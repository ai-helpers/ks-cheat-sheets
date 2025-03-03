# References

- [Keynote Slides - Parameter-Efficient Fine-Tuning (PEFT) - AI with Deep Learning](https://media.licdn.com/dms/document/media/v2/D4E1FAQEDAu58T3XaLQ/feedshare-document-pdf-analyzed/B4EZPVK9vFHAAY-/0/1734448287923?e=1736985600&v=beta&t=mYwFIyoNzZOpm3RozE-rey-wvGKqOorweo3dIFoZZfc)

# Methods finetuning

![finetuning](https://github.com/user-attachments/assets/4f602903-6861-4cac-b5c6-d2450dc6a8a0)

- Full Fine-tuning
  - Updates all model parameters simultaneously and requires substantial computational resources
  - Offers maximum adaptability but risks of catastrophic forgetting
  - Needs careful hyperparameter tuning 

- Supervised Fine-Tuning (SFT)
  - Traditional approach where model parameters are adjusted through gradient-based optimization
  - The optimization process occurs with respect to a task-specific loss function, with the model gradually refine its parameters to reduce the loss over training iterations

- Parameter-Efficient Fine-Tuning (PEFT)
  - Instead of updating all model parameters, it target a small, task-specific subset typically around 15-20% of the model's total parameters
  - It drastically reduces the computational load while preserve the majority of the model's pretrained knowledge, mitigating the risk of catastrophic forgetting
  - Adapters and prefix tuning which allow for task adaptation without a full retraining process:

  * LoRA (Low-Rank Adaptation)
    - Implements low-rank matrix decomposition of weight updates
    - Achieves parameter reduction ratios exceeding 10,000:1
    - Particularly effective for domain-specific adaptations
  * Adapter tuning
    - Introduces lightweight adapter modules between frozen transformer layers
    - Maintains original model parameters while adding minimal trainable modules
    - Resistance to catastrophic forgetting 

* Transfer Learning
  -  Adapts pre-trained models to specific domains and maintains core knowledge while adding domain-specific features
  -  Enables rapid adaptation with minimal training data
  -  Effective for related tasks and domains

* Multitask Learning
  -  Trains on multiple tasks simultaneously
  -  Prevents catastrophic forgetting across tasks
  -  Promotes shared representation learning
  -  Requires larger datasets and more complex optimization

- Task-Specific Fine-tuning
  - Optimizes model performance for single tasks and achieve high performance with limited training data
  - Risk of catastrophic forgetting on other tasks
  - Ideal for specialized applications require deep domain expertise

- Sequential Fine-tuning
  - Implements progressive learning through staged objectives
  - Allows hierarchical knowledge acquisition
  - Maintains stability through gradual adaptations
  - Effective for complex task sequences and domain progression
 
[Source - Post](https://www.linkedin.com/posts/aboniasojasingarayar_llm-finetuning-activity-7300062003375603721-Cgwd?utm_source=share&utm_medium=member_desktop&rcm=ACoAABY4zkYBTs23buQ5AEQ-XagrOSQPiyJTUNs)
