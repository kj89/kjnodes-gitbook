---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/hypersign.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: jagrat | **Latest Version Tag**: v0.1.6 | **Custom Port**: 31

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf hid-node
git clone https://github.com/hypersign-protocol/hid-node.git
cd hid-node
git checkout v0.1.6

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.hid-node/cosmovisor/upgrades/v016/bin
mv build/hid-noded $HOME/.hid-node/cosmovisor/upgrades/v016/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
