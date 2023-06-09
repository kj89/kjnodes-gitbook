# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibirufi) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:13990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:13956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:13959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (13)
```bash
peers="595a8f93897710cacc3173c9ae4d0bafda5b3879@141.94.73.93:36656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,b3a2a298c6a84c503253d120e3eee0c54cea90fd@137.184.193.235:20356,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,e08089921baf39382920a4028db9e5eebd82f3d7@142.132.199.236:21656,954598490831bce4e650593d23466bf676c04914@185.16.39.19:38656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,613e133355a43be28b31d33d13c8814d6ea0c99f@34.75.8.154:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,e1cb0df376c0f88169cb203b304d7cf26b87d1a3@149.102.158.241:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
