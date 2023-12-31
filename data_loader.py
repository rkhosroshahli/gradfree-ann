import numpy as np
import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Subset

def load_mnist_train_selection(samples_per_class=100, seed=42, batch_size=64):
    # Set a random seed for reproducibility
    # seed = 42
    # np.random.seed(seed)
    # torch.manual_seed(seed)
    rng = np.random.default_rng(seed)
    

    # Define the transformation to apply to the data
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

    # Load the original MNIST dataset
    mnist_train = torchvision.datasets.MNIST('./data', train=True, download=True, transform=transform)

    # Create an empty list to store the balanced dataset
    balanced_train_dataset = []

    # Randomly select samples from each class for the training dataset
    for i in range(10):
        class_indices = np.where(np.array(mnist_train.targets) == i)[0]
        selected_indices = rng.choice(class_indices, samples_per_class, replace=False)
        balanced_train_dataset.extend(Subset(mnist_train, selected_indices))
        
    # Check the sizes of the resulting datasets
    print("Size of balanced training dataset:", len(balanced_train_dataset))

    # Create DataLoaders for the balanced datasets    
    train_loader = DataLoader(balanced_train_dataset, batch_size=batch_size, shuffle=True)
    return train_loader

def load_mnist_train_full(batch_size=64):
    # Define the transformation to apply to the data
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
    
    train_dataset = torchvision.datasets.MNIST('./data', train=True, download=True, transform=transform)
    
    print("Size of balanced training dataset:", len(train_dataset))

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    return train_loader
    
def load_mnist_test(batch_size=64):
    # Define the transformation to apply to the data
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
    
    test_dataset = torchvision.datasets.MNIST(root='./data', train=False, transform=transform, download=True)
    
    print("Size of balanced test dataset:", len(test_dataset))

    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    return test_loader


def load_cifar10_train_selection(samples_per_class=100, seed=42, batch_size=64):
    # Set a random seed for reproducibility
    # seed = 42
    # np.random.seed(seed)
    # torch.manual_seed(seed)
    rng = np.random.default_rng(seed)
    

    # Define the transformation to apply to the data
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    # Load the original MNIST dataset
    mnist_train = torchvision.datasets.CIFAR10('./data', train=True, download=True, transform=transform)

    # Create an empty list to store the balanced dataset
    balanced_train_dataset = []

    # Randomly select samples from each class for the training dataset
    for i in range(10):
        class_indices = np.where(np.array(mnist_train.targets) == i)[0]
        selected_indices = rng.choice(class_indices, samples_per_class, replace=False)
        balanced_train_dataset.extend(Subset(mnist_train, selected_indices))
        
    # Check the sizes of the resulting datasets
    print("Size of balanced training dataset:", len(balanced_train_dataset))

    # Create DataLoaders for the balanced datasets    
    train_loader = DataLoader(balanced_train_dataset, batch_size=batch_size, shuffle=True)
    return train_loader

def load_cifar10_train_full(batch_size=64):
    # Define the transformation to apply to the data
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    
    train_dataset = torchvision.datasets.CIFAR10('./data', train=True, download=True, transform=transform)
    
    print("Size of balanced training dataset:", len(train_dataset))

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    return train_loader
    
def load_cifar10_test(batch_size=64):
    # Define the transformation to apply to the data
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    
    test_dataset = torchvision.datasets.CIFAR10(root='./data', train=False, transform=transform, download=True)
    
    print("Size of balanced test dataset:", len(test_dataset))

    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    return test_loader


def load_cifar100_train_selection(samples_per_class=100, seed=42, batch_size=64):
    # Set a random seed for reproducibility
    # seed = 42
    # np.random.seed(seed)
    # torch.manual_seed(seed)
    rng = np.random.default_rng(seed)
    

    # Define the transformation to apply to the data
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    # Load the original MNIST dataset
    mnist_train = torchvision.datasets.CIFAR100('./data', train=True, download=True, transform=transform)

    # Create an empty list to store the balanced dataset
    balanced_train_dataset = []

    # Randomly select samples from each class for the training dataset
    for i in range(100):
        class_indices = np.where(np.array(mnist_train.targets) == i)[0]
        selected_indices = rng.choice(class_indices, samples_per_class, replace=False)
        balanced_train_dataset.extend(Subset(mnist_train, selected_indices))
        
    # Check the sizes of the resulting datasets
    print("Size of balanced training dataset:", len(balanced_train_dataset))

    # Create DataLoaders for the balanced datasets    
    train_loader = DataLoader(balanced_train_dataset, batch_size=batch_size, shuffle=True)
    return train_loader

def load_cifar100_train_full(batch_size=64):
    # Define the transformation to apply to the data
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    
    train_dataset = torchvision.datasets.CIFAR100('./data', train=True, download=True, transform=transform)
    
    print("Size of balanced training dataset:", len(train_dataset))

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    return train_loader
    
def load_cifar100_test(batch_size=64):
    # Define the transformation to apply to the data
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    
    test_dataset = torchvision.datasets.CIFAR100(root='./data', train=False, transform=transform, download=True)
    
    print("Size of balanced test dataset:", len(test_dataset))

    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    return test_loader