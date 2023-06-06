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

**live-peers** (26)
```bash
peers="3519e61e653db97f5d1c7f1bec9b0072bca4d5fe@144.76.45.59:16656,8e14e58b054248a04be96e4a40d6359e93b636ac@65.108.65.94:26656,ba65c74ac5f3c56b450348dea59b4d815220aeca@142.132.151.99:15651,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:27026,8b486ec6ee6167985f6eed69817f2a04bd70bba9@65.109.61.113:22217,e6bf55bc9f08958b7518bea455423375db78d1ef@65.108.13.176:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11156,c152888de058c1ca92e43913b502b137b8c17c26@195.201.243.40:26636,3e484a1e5b0e019f1c227fb1481016161825c395@213.239.215.165:11156,5a3c424c19d9ab694190a7805a2b1a146460d752@65.108.2.27:26656,c02431ff1a4fe66dca2d3c8ccbbd51b9977d8c54@88.208.57.200:11156,6d3319970389d88f5deee9720a44fb95cad01ea2@185.144.99.96:26656,cd85e8a5ad374c3ee339d6f201a065ae9e911eb4@65.108.226.183:11156,386d9eac66143c386d645b13eb9906caeb3cb33a@82.100.58.116:26656,a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656,676272662f2bba070a820aacc7ab7cec446526be@65.109.80.176:20656,7142a4a19a87408ea6bcaf8bc2fd0265a5ccc7ad@162.55.245.219:11156,2aed12a25bfa92e40ccb95c88692735a9488a17e@65.109.92.79:37656,cc18d980216d658b76112fefd49cf2bf03d2d1cb@65.109.58.237:36589,e6bf4eca6a11035c06be529cb8c3758c2c00908f@213.170.135.20:26656,80a09a8ae70e893789110c7945cb8f324002bfed@88.98.195.228:16656,5e83e140ae6a480ec8ac714fb71e0b509227cb9a@185.144.99.18:26656,7283ce0d1cf4fd83fe826866a90b244d943fc434@38.242.248.195:11156,fcf5eb2872fdde3ce23a1bf23708434025851411@47.147.226.228:55656,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:26656,8e12ec6575dcaf4734a0bb2903e3cbb6924a9902@161.97.79.100:57656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
