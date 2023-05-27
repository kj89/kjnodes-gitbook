# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: rhye-1 | **Latest Version Tag**: v1.4.2-rc7 | **Wasm**: OFF

[Website](https://quicksilver.zone) | [Discord](https://discord.gg/quicksilverprotocol) | [Twitter](https://twitter.com/quicksilverzone)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/quicksilver-testnet](https://explorer.kjnodes.com/quicksilver-testnet)

## Public endpoints

* api: [https://quicksilver-testnet.api.kjnodes.com](https://quicksilver-testnet.api.kjnodes.com)
* rpc: [https://quicksilver-testnet.rpc.kjnodes.com](https://quicksilver-testnet.rpc.kjnodes.com)
* grpc: quicksilver-testnet.grpc.kjnodes.com:11190

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@quicksilver-testnet.rpc.kjnodes.com:11156
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@quicksilver-testnet.rpc.kjnodes.com:11159
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver-testnet/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (20)
```bash
peers="8e12ec6575dcaf4734a0bb2903e3cbb6924a9902@161.97.79.100:57656,ac6068dc650358a0c8f7b774630367ba2c70fa1f@93.190.141.68:21026,a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656,2a577a2f1a3c9e6fdcf19659af4ecc48f4525274@135.181.215.115:26776,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:27026,5a3c424c19d9ab694190a7805a2b1a146460d752@65.108.2.27:26656,e6bf55bc9f08958b7518bea455423375db78d1ef@65.108.13.176:26656,d3e80f977fe2ed85029c656e596dbb70b3bd7fee@65.109.95.178:37656,3e484a1e5b0e019f1c227fb1481016161825c395@213.239.215.165:11156,debb2e9f8892606629c5a6d63a8562879868e261@65.108.99.224:56656,1452d484454c0f93ddf3cbf987ce1b9cadd8f23f@65.21.95.180:37656,ee6bae1a6d4a1e07f1e4bc7963cabedc6b73426e@94.130.137.119:26656,8e14e58b054248a04be96e4a40d6359e93b636ac@65.108.65.94:26656,7142a4a19a87408ea6bcaf8bc2fd0265a5ccc7ad@162.55.245.219:11156,676272662f2bba070a820aacc7ab7cec446526be@65.109.80.176:20656,baa0e310137406a4071718c8028b802ce9475f9a@46.4.121.72:11156,ba65c74ac5f3c56b450348dea59b4d815220aeca@142.132.151.99:15651,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11156,3519e61e653db97f5d1c7f1bec9b0072bca4d5fe@144.76.45.59:16656,8b486ec6ee6167985f6eed69817f2a04bd70bba9@65.109.61.113:22217"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
