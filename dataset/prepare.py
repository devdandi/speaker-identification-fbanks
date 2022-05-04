import os

from torchaudio.datasets import LIBRISPEECH

def download_dataset_libri():
    isDownload = False
    if os.path.exists('LibriSpeech'):
        # print("UDAH ADA")
        isDownload = False

    else:
        isDownload = True

    dataset = LIBRISPEECH(
        root="dataset/",
        download=isDownload
    )


download_dataset_libri()