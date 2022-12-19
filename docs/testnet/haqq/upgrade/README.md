---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.0 | **Custom Port**: 35

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf haqq
git clone https://github.com/haqq-network/haqq.git
cd haqq

# Build binaries
git checkout v1.3.0
make build
mkdir -p $HOME/.haqqd/cosmovisor/upgrades/v1.3.0/bin
mv build/haqqd $HOME/.haqqd/cosmovisor/upgrades/v1.3.0/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
