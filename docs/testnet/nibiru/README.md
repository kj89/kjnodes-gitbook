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
peers="b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,8a2e384b898a00dcf8052d129d6beb9f8f5ef86b@5.75.232.237:26656,e3fc96a180861a923807d29b748a6cddd3230a8f@5.189.171.168:26656,5160aa16c18a37d25c3e667c80de83279715f2aa@195.2.75.252:26656,db832cabda2d29d8e2570c0f3a5797098db5a7b8@135.181.25.101:26656,03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656,04c7b4c7b1ca40e04e767925c08846d2951f5425@34.23.168.27:26656,4dc627534292d408d9087b7d62e59a10fdf99e7f@65.109.60.19:46656,b6fe0cb29a6cca2acd41aade05c46272db5c7c0c@209.126.83.209:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,6173aa0fb340ab41724d72339d164a86e7a6d0ac@185.229.119.95:26656,370107c2f46450646cfe87d59bd6684ec2231064@85.239.241.80:26656,595a8f93897710cacc3173c9ae4d0bafda5b3879@141.94.73.93:36656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,cb825bccee49827c07dce19878c8790c67222a54@91.107.132.237:26656,0cc5236b8a37e89af65c8504982ae0eb5b01e004@178.20.47.61:26656,5b2614774a890a7383e9700e4fc8fa202517ec74@144.91.97.6:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,613e133355a43be28b31d33d13c8814d6ea0c99f@34.75.8.154:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
