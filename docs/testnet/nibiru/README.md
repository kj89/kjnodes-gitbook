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

**live-peers** (17)
```bash
peers="7f8bd4eaf6b9b213fd7b89ceefc517bcaa517d24@5.9.147.22:22656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,8a2e384b898a00dcf8052d129d6beb9f8f5ef86b@5.75.232.237:26656,e1cb0df376c0f88169cb203b304d7cf26b87d1a3@149.102.158.241:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,5b2614774a890a7383e9700e4fc8fa202517ec74@144.91.97.6:26656,5160aa16c18a37d25c3e667c80de83279715f2aa@195.2.75.252:26656,a5455fdd70a915023bb4902143704430793c3e68@162.55.163.78:26656,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,dfdfca675e009578b775d7febace9d15d97c3755@207.180.224.21:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
