---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/archway.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: constantine-3 | **Latest Version Tag**: v1.0.0-rc.1 | **Custom Port**: 156

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf archway
git clone https://github.com/archway-network/archway.git
cd archway
git checkout v1.0.0-rc.1

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.archway/cosmovisor/upgrades/v0.6.0/bin
mv build/archwayd $HOME/.archway/cosmovisor/upgrades/v0.6.0/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
