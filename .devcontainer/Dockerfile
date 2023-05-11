FROM ubuntu:22.04

ENV PYTHON_VERSION 3.8.12
ENV DEBIAN_FRONTEND=noninteractive
#Set of all dependencies needed for pyenv to work on Ubuntu
RUN apt-get update \ 
    && apt-get install -y --no-install-recommends make build-essential libssl-dev libpq-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget ca-certificates curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev mecab-ipadic-utf8 git postgresql-client telnet unzip zlib1g-dev

RUN curl https://cli-assets.heroku.com/install.sh | sh
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && apt-get install -y nodejs

ARG USERNAME=codeany
RUN useradd -ms /bin/bash $USERNAME
USER $USERNAME
WORKDIR /home/$USERNAME

# Set-up necessary Env vars for PyEnv
ENV PYENV_ROOT /home/$USERNAME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# Install pyenv
RUN set -ex \
    && curl https://pyenv.run | bash \
    && pyenv update \
    && pyenv install $PYTHON_VERSION \
    && pyenv global $PYTHON_VERSION \
    && pyenv rehash \
    && python3 -m pip install --no-cache-dir --upgrade pip \
    && python3 -m pip install --no-cache-dir --upgrade setuptools wheel virtualenv pipenv pylint rope flake8  mypy autopep8 pep8 pylama pydocstyle bandit notebook twine

ENV PATH=$PATH:"/home/codeany/.local/bin"

RUN echo 'alias python=python3' >> ~/.bashrc && \
    echo 'export PIP_USER=yes' >> ~/.bashrc && \
    echo 'alias pip=pip3' >> ~/.bashrc && \
    echo 'alias psql="psql mydb"' >>  ~/.bashrc

COPY ./build-assets/heroku_config.sh /home/$USERNAME/.theia/heroku_config.sh
RUN echo 'alias heroku_config=". $HOME/.theia/heroku_config.sh"' >> ~/.bashrc

COPY ./build-assets/make_url.py /home/$USERNAME/.theia/make_url.py
RUN echo 'alias make_url="python3 $HOME/.theia/make_url.py "' >> ~/.bashrc

COPY ./build-assets/http_server.py /home/$USERNAME/.theia/http_server.py
RUN echo 'alias http_server="python3 $HOME/.theia/http_server.py "' >> ~/.bashrc


USER root
RUN chown -R $USERNAME:$USERNAME /home/$USERNAME/.theia

CMD ["tail", "-f", "/dev/null"]

# Allows proxy to work for react/drf on cloud ide's
ENV DANGEROUSLY_DISABLE_HOST_CHECK=true
