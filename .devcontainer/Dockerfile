FROM ros:jazzy

# update package index
RUN apt-get update

# install python stuff
RUN apt install -y --no-install-recommends \
  python3-full \
  python3-dev \
  python3-pil \
  python3-pip \
  python3-setuptools \
  python3-tk \
  python3-venv \
  python3-wheel

# Create and activate Python virtual environment
RUN python3 -m venv /opt/venv
# Set the PATH to prioritize virtual environment binaries
ENV PATH="/opt/venv/bin:$PATH"

# is this even needed?
# RUN python -m venv venv && . venv/bin/activate

RUN pip install keyboard && pip install pyserial

# install ros demo packages
RUN apt-get install -y \
  ros-${ROS_DISTRO}-demo-nodes-cpp \
  ros-${ROS_DISTRO}-demo-nodes-py && \
  rm -rf /var/lib/apt/lists/*

# Append the source command to .bashrc
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc

# Default command to keep the container running
ENTRYPOINT [""]