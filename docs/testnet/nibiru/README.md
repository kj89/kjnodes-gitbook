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

**live-peers** (20)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,5e65a3d32678a7206d006f899be707c130a9ada1@162.55.234.70:55356,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,ecbf8f3be0826e9905dc0dfff5c02d922cf768b9@65.21.56.168:26656,b6fe0cb29a6cca2acd41aade05c46272db5c7c0c@209.126.83.209:26656,e1cb0df376c0f88169cb203b304d7cf26b87d1a3@149.102.158.241:26656,d5d51ad6226922fe0a85de41e972722021e6b982@138.201.31.28:26656,0bec869738691df5d0c1f40348c95cd256382f26@89.116.31.114:26656,668ae8cb141c97d3fc27930bda216d94459e2790@135.181.253.203:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,370107c2f46450646cfe87d59bd6684ec2231064@85.239.241.80:26656,8a2e384b898a00dcf8052d129d6beb9f8f5ef86b@5.75.232.237:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,61c3b93bc69ed2b209ffbf959c4a5701e6eb7416@95.217.163.250:26656,595a8f93897710cacc3173c9ae4d0bafda5b3879@141.94.73.93:36656,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,436cb422506a1b3fc9c4e1e5920625e49babe161@185.219.142.214:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
