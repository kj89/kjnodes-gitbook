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

**live-peers** (29)
```bash
peers="856f1b729ccb2d0f12bc638ddb71ae49bece70f4@31.220.90.89:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,668ae8cb141c97d3fc27930bda216d94459e2790@135.181.253.203:26656,049f949ef374eb0202685e17742241005acde129@38.242.152.36:26656,3a5d2bd306d6a0b842e5b14dfd1fc5a1069b55d1@14.162.213.215:20156,8a2e384b898a00dcf8052d129d6beb9f8f5ef86b@5.75.232.237:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,12a67161a0424228817ef4d5b7a8157797422bd7@144.76.118.130:26656,391ce347a9f0745a1f50126fcc1f9a878bacd8fe@184.174.32.55:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,266c6ed8ed0a5e034bc71843b849a776abce7cbc@217.76.58.18:39656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,93b0696cd10a3d683c1cf28641ff210d316954da@89.117.63.232:26656,129586ad8f2e42c87d8811012107581b3eb0a1b1@146.0.35.40:26656,f31536c1f70fb1a8127c1f412bbccef4d1a19e20@195.14.6.2:26656,015a39332269be67fb95317038e8c9c57c6ca121@167.71.209.28:39656,2fe037c0e7a8f3da20ef50f20712b55fd52a9b8b@144.91.110.211:29656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,83be009ed822ad05d877c26bfa457c95551128c0@167.99.249.130:26656,0e6e70a3341b45cf025d0d0576a51d774b6cba61@31.220.88.173:39656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,f8c257cf4791ba315ac8b291a065e825afd7310c@195.201.85.236:11656,31dfb28f50d112bc4090eb98bf0610fbf7a8cbc5@159.69.56.78:11656,d31e21c9ddc00e2ab2bbfbafde3810e2d4370993@31.220.94.117:39656,ad41ef68f4740d5be84ff54c34b0331b02ff4ae4@85.10.193.246:29656,6c37c542748d1d78c3c0d96eb7c5f1af5ee6a770@213.202.211.70:26656,39ce82b6613c327f2bbc4cedc3a25dbf0bf8094e@38.242.252.137:26656,d4bb11fc3fdf834e13a803f159dfe12851c4b1c1@86.48.3.201:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
