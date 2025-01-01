import base64
import json
import requests
from PIL import Image
import io
import torch
from torchvision.transforms import ToPILImage

class OpenrouterNode:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_url": ("STRING", {
                    "multiline": False,
                    "default": "https://openrouter.ai/api/v1/chat/completions"
                }),
                
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "describe image"
                }),
                "temperature": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.1,
                }),
            },
            "optional": {
                "model": ("STRING", {
                    "multiline": False,
                    "default": "anthropic/claude-3-haiku:beta"
                }),
                "image_input": ("IMAGE", {
                    "optional": True
                }),

                }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_completion"
    CATEGORY = "OpenRouter"

    def get_completion(self, base_url, api_key, prompt, temperature, model=None, image_input=None):
        try:
            
            if model is None:
                headers = {
                    "api-key": f"{api_key}",
                    "Content-Type": "application/json"
                }
            else:
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                }

            # Initialize messages with proper structure
            messages = [{
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }]

            import numpy as np

            if image_input is not None:
                if isinstance(image_input, torch.Tensor):
                    i = 255. * image_input[0].cpu().numpy()
                    # Create PIL Image
                    img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

                elif isinstance(image_input, Image.Image):
                    img = image_input
                else:
                    return ("Error: Unsupported image_input type.",)
                
                buffered = io.BytesIO()
                img.save(buffered, format="JPEG")
                img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
                image_data = f"data:image/jpeg;base64,{img_str}"

                image_message = {
                    "type": "image_url",
                    "image_url": {
                        "url": image_data
                    }
                }
                
                # Append the image message to the content list
                messages[0]["content"].append(image_message)

            if model is None:
                body = {
                "messages": messages,
                "temperature": temperature
            }
            else:
                body = {
                    "model": model,
                    "messages": messages,
                    "temperature": temperature
                }
            
            response = requests.post(base_url, headers=headers, data=json.dumps(body), timeout=(60, 60))
            response.raise_for_status()

            response_json = response.json()

            if "choices" in response_json and len(response_json["choices"]) > 0:
                assistant_message = response_json["choices"][0].get("message", {}).get("content", "")
                return (assistant_message,)
            else:
                return ("No response from the model.",)

        except requests.exceptions.RequestException as req_err:
            return (f"Request Error!!: {str(req_err)}",)
        except Exception as e:
            return (f"Error: {str(e)}",)

# Node registration
NODE_CLASS_MAPPINGS = {
    "OpenrouterNode": OpenrouterNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OpenrouterNode": "OpenRouter Node"
}
