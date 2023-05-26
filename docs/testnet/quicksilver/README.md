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

**live-peers** (18)
```bash
peers="3519e61e653db97f5d1c7f1bec9b0072bca4d5fe@144.76.45.59:16656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:27026,a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656,c152888de058c1ca92e43913b502b137b8c17c26@195.201.243.40:26636,ee6bae1a6d4a1e07f1e4bc7963cabedc6b73426e@94.130.137.119:26656,e6bf55bc9f08958b7518bea455423375db78d1ef@65.108.13.176:26656,7142a4a19a87408ea6bcaf8bc2fd0265a5ccc7ad@162.55.245.219:11156,ac6068dc650358a0c8f7b774630367ba2c70fa1f@93.190.141.68:21026,ba65c74ac5f3c56b450348dea59b4d815220aeca@142.132.151.99:15651,cd85e8a5ad374c3ee339d6f201a065ae9e911eb4@65.108.226.183:11156,5a3c424c19d9ab694190a7805a2b1a146460d752@65.108.2.27:26656,3e484a1e5b0e019f1c227fb1481016161825c395@213.239.215.165:11156,1452d484454c0f93ddf3cbf987ce1b9cadd8f23f@65.21.95.180:37656,676272662f2bba070a820aacc7ab7cec446526be@65.109.80.176:20656,2a577a2f1a3c9e6fdcf19659af4ecc48f4525274@135.181.215.115:26776,4abe3e468eeb3a957d34efec57b01a4add92904e@185.16.39.51:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11156,392a7ec2683e288866c353b7a8ac9ecc4e7b4bfc@142.165.207.19:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
