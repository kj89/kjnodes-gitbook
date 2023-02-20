---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.6.0-RC3 | **Custom Port**: 44

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf lava
git clone https://github.com/lavanet/lava.git
cd lava
git checkout v0.6.0-RC3

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.lava/cosmovisor/upgrades/v0.6.0-RC3/bin
mv build/lavad $HOME/.lava/cosmovisor/upgrades/v0.6.0-RC3/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
