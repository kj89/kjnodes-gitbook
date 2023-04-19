# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: quicksilver-2 | **Latest Version Tag**: v1.2.9-hotfix.0 | **Wasm**: OFF

[Website](https://quicksilver.zone) | [Discord](https://discord.gg/quicksilverprotocol) | [Twitter](https://twitter.com/quicksilverzone)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/quicksilver/quickvaloper1fqfgpwdngmmay6ah7mg9y4k7ayykpzu6l3ht2m)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/quicksilver/quickvaloper1fqfgpwdngmmay6ah7mg9y4k7ayykpzu6l3ht2m) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/quicksilver](https://explorer.kjnodes.com/quicksilver)

## Public endpoints

* api: [https://quicksilver.api.kjnodes.com](https://quicksilver.api.kjnodes.com)
* rpc: [https://quicksilver.rpc.kjnodes.com](https://quicksilver.rpc.kjnodes.com)
* grpc: quicksilver.grpc.kjnodes.com:11090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@quicksilver.rpc.kjnodes.com:11656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@quicksilver.rpc.kjnodes.com:11659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (29)
```bash
peers="914bed178748772d7578d119cb2dc89d5076b9f4@135.181.223.115:2390,26d23125db7493486dc9931b4181425d725e4ac6@65.109.55.186:20656,a1f5e0b68f36091d5fc8f30aba914b6c191f21fa@65.108.128.201:11156,c2a44958de52a8656eba9eedaf88205f27686ffd@46.4.23.42:11656,50a40c5aba326798ea9520ac0a1207e22a540a0e@95.214.55.100:26556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,161f453c9ff27f3120ec5078f56b505316fbc720@65.108.6.45:61156,71b753819eb653e99e6a825b80af20ca9bccb087@135.125.163.63:24666,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,0521c200a3dc430927978fb2c66293b8481fc3ae@198.244.203.181:26656,e72108879602113f6661507b583ff8b5616f06c6@95.217.202.49:31656,6f80fa3110d45fa7cf08fe7df94cf9f60da8ad4a@178.63.67.112:26656,08ab5be08f12754381c0fd088bb36d9d294f54c6@65.109.21.74:26656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,ce593f9bffc471ba4b980a435a3e2f8eaa5b464e@34.89.247.21:26656,96bd0e87a5e5b88e8ce637aa3c7aa4f4803b1d03@51.195.234.240:26656,a4f29a68180d1a1c931b50e2438a63b0d45d6915@89.58.48.229:26656,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
