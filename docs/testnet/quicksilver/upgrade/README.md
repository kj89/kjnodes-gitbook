---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: innuendo-4 | **Latest Version Tag**: ${LATEST_VERSION_TAG} | **Custom Port**: 11

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf quicksilver
git clone https://github.com/ingenuity-build/quicksilver.git
cd quicksilver

# Build binaries
git checkout ${LATEST_VERSION_TAG}
make build
mkdir -p $HOME/.quicksilverd/cosmovisor/upgrades/v0.10.8/bin
mv build/quicksilverd $HOME/.quicksilverd/cosmovisor/upgrades/v0.10.8/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
