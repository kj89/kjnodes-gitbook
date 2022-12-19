---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/okp4.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: okp4-nemeton-1 | **Latest Version Tag**: v3.0.0 | **Custom Port**: 36

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf okp4d
git clone https://github.com/okp4/okp4d.git
cd okp4d

# Build binaries
git checkout v3.0.0
make build
mkdir -p $HOME/.okp4d/cosmovisor/upgrades/genesis/bin
mv target/dist/okp4d $HOME/.okp4d/cosmovisor/upgrades/genesis/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
