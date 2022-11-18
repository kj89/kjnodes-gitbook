# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-3 | **Latest Version Tag**: v0.10.1 | **Wasm**: OFF

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

**live-peers** (21)
```
peers="47a7fac621a79649519eadbb8deb92d33bb3259b@161.97.82.203:26256,a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656,f7edad3ff5a85d039e7de12067c63064c5b42d63@46.4.121.72:11656,433f85361545a434ad6b4202e2f373e4894ecf39@142.132.151.99:15619,dc88be3a0075ce429a423237abe223a9528ce0df@65.108.204.119:31656,a854277e77b0ac095e53156266cdc39ad4b13b2f@142.132.205.94:15619,20b6b3f6c0927c14a2348f5e378b98cb8596fc06@34.105.195.160:26656,0551eaa0db7097274410ee27a71672817e314b83@167.235.245.191:26656,66f9d8f52a4637dc9215cdaa8dc2977633e52bbf@95.217.144.121:26656,03332cdbc3d354846a18992effbb8c20aa28f52a@65.21.133.125:28656,2096650d8586b858d3369205f3b46ac4c765bc8e@65.109.53.155:26656,41f7d7004cace7bd1760a5f980a86123700c8f1d@185.146.148.116:26656,711b97aa5956c6ce95c05895faa6c3ad3c04d440@135.181.59.162:11156,1c1ca90d704c22844570d57039ccf2e8f58e475d@80.64.208.123:26656,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,392a7ec2683e288866c353b7a8ac9ecc4e7b4bfc@142.165.207.19:16656,5c6bfcfd42e8a4cf7960cf8b1860eed3de17196d@65.108.75.237:2010,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:28656,8ff8a186fe9cbc70d0f34891fa051f87e561a48b@158.160.0.93:26656,7fe3007cba4de49584cbdad9489ffecfc9651c57@65.108.79.246:26673,9e4c87dc3a2365fe44ab52a9e22a43cc6378a935@142.132.199.27:21026"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
