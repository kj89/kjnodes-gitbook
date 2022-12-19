---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/aura.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: euphoria-2 | **Latest Version Tag**: euphoria_v0.4.2 | **Custom Port**: 17

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf aura
git clone https://github.com/aura-nw/aura.git
cd aura

# Build binaries
git checkout euphoria_v0.4.2
make build
mkdir -p $HOME/.aura/cosmovisor/upgrades/v0.4.2/bin
mv build/aurad $HOME/.aura/cosmovisor/upgrades/v0.4.2/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
