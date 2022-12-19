---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.4 | **Custom Port**: 15

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf uptick
git clone https://github.com/UptickNetwork/uptick.git
cd uptick

# Build binaries
git checkout v0.2.4
make build
mkdir -p $HOME/.uptickd/cosmovisor/upgrades/genesis/bin
mv build/uptickd $HOME/.uptickd/cosmovisor/upgrades/genesis/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
