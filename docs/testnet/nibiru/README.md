# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:39090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (30)
```bash
peers="8a2e384b898a00dcf8052d129d6beb9f8f5ef86b@5.75.232.237:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,7b69fec8f71ccb56b0a2d7ddc07a92c2982a77d1@34.125.91.236:26656,b15ff5df6bea62dc567f5b628bb922a4185621b6@5.75.196.224:26656,4849121004b25be32ca2c80fdfed3f7991515d88@38.242.207.34:39656,e782ece88fe9abd589f1c2f712f3e891c1f3982a@79.137.203.27:26656,17d683da420ce5eaa3fe1b9699b6b7720e4c5483@158.220.100.251:26656,5b4b12ded2c0db5f29345580b507156ca5399053@31.220.84.69:26656,668f3f60a0ff3f9fcbaf8551782f71de1cc767a9@89.116.24.215:26656,b87b7560521e022768eebc92247eb1c19cebcdc1@172.98.12.182:26656,6c37c542748d1d78c3c0d96eb7c5f1af5ee6a770@213.202.211.70:26656,c5f0bb310407e9a8974fb810a7e7d65e7e529554@65.21.250.242:26656,f31536c1f70fb1a8127c1f412bbccef4d1a19e20@195.14.6.2:26656,d191900c45d3df1611aa48c1a3bf24f851dc25c6@165.227.155.35:26656,f4a8fb180fbbb4c44e7721368cbc6ce3f9fc47e1@5.189.140.55:26656,e6eb04d29739ccb134b4c7be12c774a78eb0f875@142.132.148.174:36656,7d3867934f0664832f782e3579e30686b069c473@109.123.250.109:26656,43645ff839bca01dec1ecfa243d144ef5a87c3bc@109.123.243.4:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,3bb1549a6b7536e673bb8b9a036485c5ec18ce76@194.34.232.36:39656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,95e4f7c7e00838a0a217d58023042cf49c57b94b@45.141.122.68:26656,51ed3cdd1490d47ce8846592d1ff881453dd9f93@84.46.250.179:26656,a8b169470011010a9d410a5dad3458e0c94b1e21@109.123.246.113:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,766f17b24c11b5eac20cf938f619bc2e43331988@38.242.229.238:26656,f4fa2e13e64628d96f9158a6a2afbb19ebac574e@85.190.246.120:26656,fbf9b2614d834cce03453164c5014e5616ed1295@38.242.241.201:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
