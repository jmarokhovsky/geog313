FROM continuumio/miniconda3:22.11.1

RUN mkdir /home/assignment
WORKDIR /home/assignment
# Make a new conda environment named a2-env
COPY environment.yml ./
RUN conda env create -f environment.yml

# Create an assignment user
RUN echo "conda activate a2-env" >> ~/.bashrc
ENV PATH="$PATH:/opt/conda/envs/a2-env/bin"

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0"]
