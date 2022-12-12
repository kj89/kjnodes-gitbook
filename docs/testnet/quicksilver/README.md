# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-4 | **Latest Binary Version**: v0.10.8 | **Wasm**: OFF

Website: [https://quicksilver.zone](https://quicksilver.zone)


## Public endpoints

* rpc: [https://quicksilver-testnet.rpc.kjnodes.com](https://quicksilver-testnet.rpc.kjnodes.com)
* api: [https://quicksilver-testnet.api.kjnodes.com](https://quicksilver-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@quicksilver-testnet.rpc.kjnodes.com:11656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@quicksilver-testnet.rpc.kjnodes.com:11659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/quicksilver-testnet/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (16)
```
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11656,532625a997a6f891405202968607f72afe004f15@202.61.225.157:26666,926ce3f8ce4cda6f1a5ee97a937a44f59ff28fbf@65.108.13.176:26656,6c31ea769b18d7b20b2d738df7778fb9fc3fc380@18.236.225.32:26656,1c1ca90d704c22844570d57039ccf2e8f58e475d@80.64.208.123:26656,d4d83e209a2b096859821228ea17475f9a487a48@23.88.0.170:15651,c9a74cdd754a8ccc9243ac2b245e4caaa78695aa@45.85.147.96:26656,b9b8bb23e61d53ff3b293485d04ea567ebcd7933@65.108.65.94:26656,8099f8a7c95c1676982e1a23e8452f2b10b07415@65.108.78.107:22656,8a334ed2e728ca1164f8ef6ae58dd5fda31da5be@66.94.104.239:26641,858ba6bc33a6d13fdd9ddad344d788dcf91cf565@142.132.151.99:15651,bdb93c655989b2c1882339fabb013317066dda56@95.214.52.138:26676,13564ca7ffcc8fa6bcc6d405c96fe8c724ec17da@88.99.213.25:11656,3da9fbcb9ec210ec1c94ebc49f46fad3d3721e77@65.108.136.39:26651,7781c28c240e85474425040f744b501d99120d1d@195.201.108.152:11656,ca1dc45c25919c5b945f4c52c1e8470755a01225@65.108.44.149:20656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
