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

**live-peers** (26)
```bash
peers="9e91e7f45550a5ac96126037528d7e4b4287b948@217.76.63.119:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,3b5c0147311c294de8e635c853af5a0de72d43f1@65.21.131.215:26566,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,349a3441e26e7dc8a1d76f69d0acfc820942c837@89.163.215.4:39656,7224ab21604c27baa1c059055f41357155d5be80@165.22.208.217:26656,c03ac8a54e2fe73ac59d621eb0262456eca4d3d8@83.169.217.43:39656,9599e32760a56ac27d4a354c167c7b18e2362438@185.197.251.85:26656,332d1a117e3272d7afdc683e62e66d6b1a36869e@38.242.213.34:26656,efc2e75111f286ca7117ce4e196bfb7ba29f0a5e@109.123.243.16:26656,697c14302048b65f1e292a10632bda307cb6a149@38.242.199.224:26656,a48c9cc803e8161ee62d870992f696288d0ac6a0@38.242.232.182:26656,6b76406fb872cc3a4d194c4f0910cf8893f6affb@38.242.148.145:26656,00b1c55019204641cada3f3f24d0c191f760745f@194.163.149.195:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,b15ff5df6bea62dc567f5b628bb922a4185621b6@5.75.196.224:26656,62a39d64a6ce740d67c3858748f6ef8a63661826@5.199.139.189:39656,d191900c45d3df1611aa48c1a3bf24f851dc25c6@165.227.155.35:26656,f4a8fb180fbbb4c44e7721368cbc6ce3f9fc47e1@5.189.140.55:26656,83be009ed822ad05d877c26bfa457c95551128c0@167.99.249.130:26656,64d2ea39df1cf635fccb17311c245b9fdc56194a@91.107.195.121:26656,141dccaf3cbe958b9409bee5805f2be35da377e5@183.2.149.136:26656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,db832cabda2d29d8e2570c0f3a5797098db5a7b8@135.181.25.101:26656,5d55ddb4d498af6062e6e7c0cb7a670aba9b3302@68.183.65.30:26656,8a2e384b898a00dcf8052d129d6beb9f8f5ef86b@5.75.232.237:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
