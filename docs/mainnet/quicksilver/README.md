# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" alt=""><figcaption></figcaption></figure>

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
peers="a1f5e0b68f36091d5fc8f30aba914b6c191f21fa@65.108.128.201:11156,ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,fb1e7a989ff78f0bdd7828dc3ade95dcd67cd5d0@65.109.116.151:15656,06230bbaabb6c9c6223275b57d8e10fc609ae7ba@51.89.7.184:26633,71b753819eb653e99e6a825b80af20ca9bccb087@135.125.163.63:24666,43b97f492bf47b455b7b275c396b1840f4eb336d@142.132.139.101:26656,6f80fa3110d45fa7cf08fe7df94cf9f60da8ad4a@178.63.67.112:26656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,625eeb91fcc6242798f53426540825e5b37c7670@185.144.99.16:36656,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,41caa4106f68977e3a5123e56f57934a2d34a1c1@185.16.39.137:27026,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,3bd708547317e9efd8d63d8a51c5bc32d11f4840@138.201.32.103:26056,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,d0c81152bc586896c6c2a4dba15a4351742768d2@65.109.90.169:46656,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,2309e82e7200ac8a81f1e1f57b3ee604a20af853@51.79.177.229:26667,96b7605dbf13dbf0df2c3ac4f076397a9f351c6b@88.98.195.228:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,e72108879602113f6661507b583ff8b5616f06c6@95.217.202.49:31656,b4bcce87121963e1e97619dc135f2eb1a9fd5dfc@88.198.32.17:36656,f736b49c260e11d3f81a5d99814eaeda396c1597@18.138.35.164:26656,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
