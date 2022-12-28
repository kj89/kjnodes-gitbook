# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-testnet-2 | **Latest Version Tag**: v0.16.3 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)


## Public endpoints

* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (23)
```
peers="c08c4d5060697a644838403329be5742bdb4c67f@65.109.92.240:11036,5e65a3d32678a7206d006f899be707c130a9ada1@162.55.234.70:55356,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,9ca622adcf1ef0e7348551d4f79268f706cd3a88@65.108.195.235:36656,a4a0b5b90dbcc92006e7d05d7f6521f120520116@34.75.178.18:26656,a422bbf59756a9584ddc6f97a8b96bb15b596db7@34.73.61.37:26656,794f2f7e5bb4e9b1e7e752c3d7df76a8db824151@65.109.30.12:61756,dcbbe532327e3843174903d39c42fa3d6aee9244@194.146.12.146:26656,756a7ac7c297a6b0c5015501ad7ad484867c8c96@213.246.39.53:26656,528ac8cfeefadd4d66d87118ae0dae4db1d1d14e@173.249.14.243:26656,21e949ee5e19df867434fa145e26c8982e325c2a@185.211.6.44:26656,a4cad01b032d61534892a3c406094a7f21701e4e@209.97.133.113:39656,38d128d24e7d9cbdd80227004a7ca0fa129109b5@65.109.92.148:60656,5b38a5b453dd532b280aeb6ad05383ea4e22171f@138.197.183.235:26656,858ddaf58e566918591802ba04ce3647c5b01707@65.109.106.91:15656,7b1e85537e3f917b6858df7694cdd08088751cab@173.212.240.206:26656,d67d2bae772c3d44123a7495d56c568a185717f8@213.239.216.252:27656,9a1c88e3ea10bbfa197ec709a6ce5c4601190e0c@217.76.48.55:26656,f5e2f92458edf21b32def9fc48d7118fcd770269@161.97.144.34:26656,ab0749012b43240d8c36fb3c65284db1b2f52784@5.161.101.185:26656,3997242f9646ca642932852b7577ddb9976e0396@5.199.130.53:26656,5eecfdf089428a5a8e52d05d18aae1ad8503d14c@65.108.141.109:19656,5ef59d8905bbd2bff62e06c391bfcccd5b4f23a9@188.34.202.151:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
