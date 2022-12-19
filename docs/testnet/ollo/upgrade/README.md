---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Custom Port**: 32

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf ollo
git clone https://github.com/OLLO-Station/ollo.git
cd ollo

# Build binaries
git checkout v0.0.1
make build
mkdir -p $HOME/.ollo/cosmovisor/upgrades/genesis/bin
mv bin/ollod $HOME/.ollo/cosmovisor/upgrades/genesis/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
