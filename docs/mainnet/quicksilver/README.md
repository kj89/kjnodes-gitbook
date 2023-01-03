# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: quicksilver-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://quicksilver.zone) | [Discord](https://discord.gg/quicksilverprotocol) | [Twitter](https://twitter.com/quicksilverzone)


## Public endpoints

* rpc: [https://quicksilver.rpc.kjnodes.com](https://quicksilver.rpc.kjnodes.com)
* api: [https://quicksilver.api.kjnodes.com](https://quicksilver.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@quicksilver.rpc.kjnodes.com:11656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@quicksilver.rpc.kjnodes.com:11659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/quicksilver/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (23)
```
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,0c1d930abb6561cab37b9df5bc6af285e311ab0f@65.108.109.240:26656,0307e98cceb81b5f075ee69f53c0032940dea98c@65.108.43.113:26656,e50848e299c7909245a9af690341ff27e21f7b69@65.109.49.111:56656,43b97f492bf47b455b7b275c396b1840f4eb336d@142.132.139.101:26656,a1688942f8e51e3a372bbf0123d4a0326377e5ba@54.37.129.164:48656,9bb9b69768308bbaf2edc092a4b6cea76490422a@94.23.192.227:30572,1be3e5e90749396a3c2a07584a7c07337983d042@95.214.53.46:56656,65b1a372b38661db4ff450ed03c195a17bbade08@65.109.27.75:46656,5f0c0411e34e1c7d0b9c53749d90a923b5e8c625@65.21.133.125:35656,e09b47db9c221a9d064069befcc471d949d2c28d@45.14.135.159:15620,c8b01e6700d048b1aae34d76f5c56511b2a90ab1@57.128.133.24:26656,3a5d0b97feb595375c24665dcf17d793be129e8b@51.89.155.2:28656,96b7605dbf13dbf0df2c3ac4f076397a9f351c6b@88.98.195.228:26656,e64a4e480a2971c339fa06a58293e8e060082ad5@185.16.36.134:26656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,4559f4c24037bfad4791b2a6d6d5c769a16cad53@65.109.92.79:15656,b4bcce87121963e1e97619dc135f2eb1a9fd5dfc@88.198.32.17:36656,3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,5fa47201aa5208c30982b6f9d8ca44222d256fc5@51.91.70.90:48656,5fe7dc208641e3e730867c49b396cc7e248969fc@88.208.34.134:26656,1fa96b3e411a4ec5c6dd54389b6e7dff034f45c9@91.223.3.188:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
