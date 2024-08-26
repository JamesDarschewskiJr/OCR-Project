Here is the project I did with Consilio over the course of my six week internship.

The goal of this project was to develop a Next Gen OCR prototype that is comparable to current systems. 
While the final results of the project did not indicate that vision language models (VLMs) outperform current OCR systems like Tesseract, Phi-3-Vision was close.
Phi-3-Vision was more searchable than Tesseract was, as it dropped fewer words and had errant spacing less often than Tesseract, which is an important takeaway for the eDsicovery industry.

The ground truth for this project was Moby Dick. 
The book was broken down into chapters for analysis since it would be too unwieldy to put into the models on its own.
This gave me 136 data points to compare Tesseract, Phi-3-Vision, Florence2, and LLaVA-NeXT.

Tesseract was the best performing, with accuracy and precision numbers around 90%.
Phi-3-Vision was next, which was around 85% for accuracy and precision.
Florence2 was third, which had around 50% accuracy and precision.
Florence2 is a lightweight model that cannot be prompt engineered, so it is more suited for being fine-tuned.
The only prompt that worked for Florence2 for this task was <OCR>.
LLaVA-NeXT was the worst model.
My suspicion for LLaVA-NeXT performing so badly was that the low token numbers (only 4096 tokens) caused for the VLM to hallucinate and repeat the same line over and over.

While VLMs did not perform at as high of a level as Tesseract, there are two main takeaways from this experiment.
1. Vision Language Models are still a relatively new technology that are going to improve as models are updated and new models are released.
2. There was no fine-tuning for any of these models, everything that was part of this project was right out of the box.
