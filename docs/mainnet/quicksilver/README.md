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

**live-peers** (31)
```bash
peers="c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,c0beca70dbd3ef5bb433f7aa280d56d2a150bbd3@95.214.52.144:26656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,ae44851a5d63d70382c1621bc7727db2a40d10d0@88.99.164.158:21026,f736b49c260e11d3f81a5d99814eaeda396c1597@18.138.35.164:26656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,ce3837aa07eb0967c024d4c592f7c2730754bdd8@157.90.179.182:16656,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,61d96fee29a9615c208c4db72526d23b45094cb4@65.108.195.30:36656,3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,161f453c9ff27f3120ec5078f56b505316fbc720@65.108.6.45:61156,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,71d1e3336f41475c3dfc247aa77a8842a24c369a@144.91.80.32:11656,0a3860f9d3c27b34910fe8660240ae55699b55c2@84.244.95.245:26656,4de2811fd20d33110daf62223975beccecbe55a0@15.235.114.195:26656,040c3f32308aa75fa0f4d3b1b7c88ab5d45058a9@65.109.19.176:26656,3bd708547317e9efd8d63d8a51c5bc32d11f4840@138.201.32.103:26056,cdd8e0e425f107d249389a5e4cea3494185d4a3a@193.70.45.106:11156,b4bcce87121963e1e97619dc135f2eb1a9fd5dfc@88.198.32.17:36656,34047b39deae3110158c2bf7359e4a1b559dd8ca@159.89.171.207:26656,625eeb91fcc6242798f53426540825e5b37c7670@185.144.99.16:36656,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,e8a9be589ae825aa4368c6a00b50b7031d5de58b@65.108.78.107:21609,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.98:26656,0abbbe9eb0539d87849671384fa0e7905f4b8fa8@213.170.135.153:26546,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
