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

**live-peers** (30)
```bash
peers="61d96fee29a9615c208c4db72526d23b45094cb4@65.108.195.30:36656,67c3cc1397d0a0f03a45d4cae6ff3380be7364f9@95.217.229.18:11656,f73b2b887e7d1c01a3d753db359a0058e634e767@65.108.201.154:2090,71b753819eb653e99e6a825b80af20ca9bccb087@135.125.163.63:24666,0a226e70ceb7a4123e66216d1ed83ef22ed8a187@185.119.118.118:2000,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,4aa307d4ce413837a3da019e966d8115fb4c1467@198.244.229.218:26656,149a25417349d70f5e5127a5eb634dbfaf6e6c3a@142.165.207.19:56656,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,6f80fa3110d45fa7cf08fe7df94cf9f60da8ad4a@178.63.67.112:26656,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,a4f29a68180d1a1c931b50e2438a63b0d45d6915@89.58.48.229:26656,625eeb91fcc6242798f53426540825e5b37c7670@185.144.99.16:36656,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,161f453c9ff27f3120ec5078f56b505316fbc720@65.108.6.45:61156,ce593f9bffc471ba4b980a435a3e2f8eaa5b464e@34.89.247.21:26656,3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,d0c81152bc586896c6c2a4dba15a4351742768d2@65.109.90.169:46656,d2517139cf7c20ebdad682dfaeb2c34822a255b6@31.223.32.35:19656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
