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

**live-peers** (27)
```bash
peers="d478d4a34de532833ec1c4df65f3b79f77265f17@35.229.110.80:26656,d31e21c9ddc00e2ab2bbfbafde3810e2d4370993@31.220.94.117:39656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,05b0e8da493f0be9fd94350da52fb59c54cc897f@161.97.150.23:26656,528ec57584b93cfe8ca5f306856670a55446da60@184.174.32.147:26656,39ce82b6613c327f2bbc4cedc3a25dbf0bf8094e@38.242.252.137:26656,391ce347a9f0745a1f50126fcc1f9a878bacd8fe@184.174.32.55:26656,fb0d5b5d4d9d29e13ab0e11f7d58eac68f373554@194.163.153.99:26656,83be009ed822ad05d877c26bfa457c95551128c0@167.99.249.130:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,3a0b54203d91571398a5b4538a938fd464c4d871@176.117.185.56:40656,d118e12997ceb666f5548dda4b0a2990ac94e0ac@185.217.126.85:39656,f31536c1f70fb1a8127c1f412bbccef4d1a19e20@195.14.6.2:26656,3bb1549a6b7536e673bb8b9a036485c5ec18ce76@194.34.232.36:39656,f17b170bdd5ded247d9f5ad4e00fed553a7b510a@38.242.208.234:62956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,93b0696cd10a3d683c1cf28641ff210d316954da@89.117.63.232:26656,f1f742db7f1190b1d7d8812beb8b2acb092a80c5@194.233.73.34:39656,96f253c371a7f7f854faf7ffc5e0ee9fc4f8dd7f@165.227.32.93:26656,9f2396fab4423c96fa7315ec9ddbb48da42e94da@31.220.90.218:39656,3e7ff1b1fa8626812b1ab8acf84a8b60518a8c10@65.109.88.254:34656,3a5d2bd306d6a0b842e5b14dfd1fc5a1069b55d1@14.162.213.215:20156,549a5eb615e8560105f3801315a07c49c1804f48@158.220.98.245:26656,0e6e70a3341b45cf025d0d0576a51d774b6cba61@31.220.88.173:39656,3edbefe333daf987dea52dd53e776add12483e70@193.203.15.44:26656,0e90ac8e15b040c2a158b68f25299fc32a9d5940@89.117.57.25:26656,5860889b038fc6be32f178c0692abc51aad6bfe1@86.48.0.102:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
