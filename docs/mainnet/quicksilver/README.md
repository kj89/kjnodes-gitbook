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
peers="1b569bf57da79df4f85d207a161a97626988af76@65.109.92.241:20026,d5a9c9ae08f0d30e36c8f64eca046fc52b00561e@65.109.92.160:26656,6053a39e67c6bae83430e354f53d99e160e4964b@65.109.28.177:28656,51070ba609ede6d7eb334b8cf0ed585f2b1ab66b@135.181.76.99:26656,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,b00a1e8869d0a8327f12f12d6b63bacf15527525@213.239.207.175:32656,841efbdd6cd5c7191b5ec849499dfd9d1ea6a931@23.88.69.22:28566,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,6f80fa3110d45fa7cf08fe7df94cf9f60da8ad4a@178.63.67.112:26656,ff2055b198685f619897058a26776b9d1b73dc3c@178.63.184.129:26656,3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,5fa47201aa5208c30982b6f9d8ca44222d256fc5@51.91.70.90:48656,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,05241d21ff9e7c699bbdb4faa73da1860b6d8cd7@128.199.85.168:26656,e72108879602113f6661507b583ff8b5616f06c6@95.217.202.49:31656,ae44851a5d63d70382c1621bc7727db2a40d10d0@88.99.164.158:21026,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,08ab5be08f12754381c0fd088bb36d9d294f54c6@65.109.21.74:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
