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

**live-peers** (24)
```bash
peers="532625a997a6f891405202968607f72afe004f15@202.61.225.157:26666,c152888de058c1ca92e43913b502b137b8c17c26@195.201.243.40:26636,4abe3e468eeb3a957d34efec57b01a4add92904e@185.16.39.51:26656,8e14e58b054248a04be96e4a40d6359e93b636ac@65.108.65.94:26656,8b486ec6ee6167985f6eed69817f2a04bd70bba9@65.109.61.113:22217,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:27026,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11156,5a3c424c19d9ab694190a7805a2b1a146460d752@65.108.2.27:26656,e6bf55bc9f08958b7518bea455423375db78d1ef@65.108.13.176:26656,676272662f2bba070a820aacc7ab7cec446526be@65.109.80.176:20656,7fe3007cba4de49584cbdad9489ffecfc9651c57@65.108.79.246:26673,d3e80f977fe2ed85029c656e596dbb70b3bd7fee@65.109.95.178:37656,2a577a2f1a3c9e6fdcf19659af4ecc48f4525274@135.181.215.115:26776,a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656,3e484a1e5b0e019f1c227fb1481016161825c395@213.239.215.165:11156,8e12ec6575dcaf4734a0bb2903e3cbb6924a9902@161.97.79.100:57656,7142a4a19a87408ea6bcaf8bc2fd0265a5ccc7ad@162.55.245.219:11156,ba65c74ac5f3c56b450348dea59b4d815220aeca@142.132.151.99:15651,ac6068dc650358a0c8f7b774630367ba2c70fa1f@93.190.141.68:21026,fcf5eb2872fdde3ce23a1bf23708434025851411@47.147.226.228:55656,25410bff2fb7312d24c11b1e990507e5e3aa40b7@135.125.5.31:48656,b2daeea17e173128d92faa96d3f52266b002be58@167.235.245.191:26656,2aed12a25bfa92e40ccb95c88692735a9488a17e@65.109.92.79:37656,c02431ff1a4fe66dca2d3c8ccbbd51b9977d8c54@88.208.57.200:11156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
