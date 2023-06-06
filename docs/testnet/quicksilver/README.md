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

**live-peers** (29)
```bash
peers="fcf5eb2872fdde3ce23a1bf23708434025851411@47.147.226.228:55656,baa0e310137406a4071718c8028b802ce9475f9a@46.4.121.72:11156,d3e80f977fe2ed85029c656e596dbb70b3bd7fee@65.109.95.178:37656,a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11156,e6bf55bc9f08958b7518bea455423375db78d1ef@65.108.13.176:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:27026,8b486ec6ee6167985f6eed69817f2a04bd70bba9@65.109.61.113:22217,c02431ff1a4fe66dca2d3c8ccbbd51b9977d8c54@88.208.57.200:11156,e6bf4eca6a11035c06be529cb8c3758c2c00908f@213.170.135.20:26656,c152888de058c1ca92e43913b502b137b8c17c26@195.201.243.40:26636,5a3c424c19d9ab694190a7805a2b1a146460d752@65.108.2.27:26656,2a577a2f1a3c9e6fdcf19659af4ecc48f4525274@135.181.215.115:26776,7142a4a19a87408ea6bcaf8bc2fd0265a5ccc7ad@162.55.245.219:11156,6d3319970389d88f5deee9720a44fb95cad01ea2@185.144.99.96:26656,cc18d980216d658b76112fefd49cf2bf03d2d1cb@65.109.58.237:36589,ba65c74ac5f3c56b450348dea59b4d815220aeca@142.132.151.99:15651,3e484a1e5b0e019f1c227fb1481016161825c395@213.239.215.165:11156,7283ce0d1cf4fd83fe826866a90b244d943fc434@38.242.248.195:11156,4abe3e468eeb3a957d34efec57b01a4add92904e@185.16.39.51:26656,5e83e140ae6a480ec8ac714fb71e0b509227cb9a@185.144.99.18:26656,78283975c2bee9b95bbf9408cc974cbab7bfe8ef@65.108.231.124:37656,676272662f2bba070a820aacc7ab7cec446526be@65.109.80.176:20656,7fe3007cba4de49584cbdad9489ffecfc9651c57@65.108.79.246:26673,8e14e58b054248a04be96e4a40d6359e93b636ac@65.108.65.94:26656,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:26656,60509a87fc6c97a013de3cdeadf5fd3eab22f896@65.109.23.114:11156,debb2e9f8892606629c5a6d63a8562879868e261@65.108.99.224:56656,b2daeea17e173128d92faa96d3f52266b002be58@167.235.245.191:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
