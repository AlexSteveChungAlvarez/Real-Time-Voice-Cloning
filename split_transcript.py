from pathlib import Path
from tqdm import tqdm
import shutil

def split_tux100h():
    with Path("datasets_root/tux100h-cvcorpus/metadata.csv").open("r", encoding="utf8") as metadata_file:
        metadata = [line.split("|") for line in metadata_file]
        texts = [item[1] for item in metadata]
        text_filenames = ["datasets_root/tux100h-cvcorpus/valid/spanish/tux-100h_new/utterance-" + item[0] + ".txt" for item in metadata]
        
        for i in tqdm(range(len(text_filenames))):
            with Path(text_filenames[i]).open("w", encoding="utf8") as output_file:
                output_file.write(texts[i])

def split_cvcorpus():
    with Path("C:/datasets/cv-corpus-13.0-2023-03-09/fr/train.tsv").open("r", encoding="utf8") as metadata_file:
        metadata = [line.split("\t") for line in metadata_file]
        texts = [item[2] for item in metadata[1:]]

        audio_filenames = [item[1] for item in metadata[1:]]
        filename_parts = [filename.split(".") for filename in audio_filenames]
        names = [part[0] for part in filename_parts]
        text_filenames = ["datasets_root/cvcorpus/train/french/cv-corpus/" + name + ".txt" for name in names]
        
        for i in tqdm(range(len(audio_filenames))):
            with Path(text_filenames[i]).open("w", encoding="utf8") as output_file:
                output_file.write(texts[i])
        
        for name in names:
            shutil.copyfile(
                    'C:/datasets/cv-corpus-13.0-2023-03-09/fr/clips/'+name+'.mp3',
                    'datasets_root/cvcorpus/train/french/cv-corpus/'+name+'.mp3'
                )

def split_pespa(gender):
     with Path("datasets_root/PeruvianSpanish/train/peruvianvoices/es_pe_"+gender+"/line_index.tsv").open("r", encoding="utf8") as metadata_file:
        metadata = [line.split("\t") for line in metadata_file]
        texts = [item[1] for item in metadata]
        audio_filenames = ["datasets_root/PeruvianSpanish/train/peruvianvoices/es_pe_"+gender+"/" + item[0] + ".txt" for item in metadata]
        
        for i in tqdm(range(len(audio_filenames))):
            with Path(audio_filenames[i]).open("w", encoding="utf8") as output_file:
                output_file.write(texts[i])


if __name__=="__main__":
    split_cvcorpus()