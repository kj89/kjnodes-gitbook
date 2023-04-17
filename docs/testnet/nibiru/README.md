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
peers="00b1c55019204641cada3f3f24d0c191f760745f@194.163.149.195:26656,3bb1549a6b7536e673bb8b9a036485c5ec18ce76@194.34.232.36:39656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,ad41ef68f4740d5be84ff54c34b0331b02ff4ae4@85.10.193.246:29656,93b0696cd10a3d683c1cf28641ff210d316954da@89.117.63.232:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,3a5d2bd306d6a0b842e5b14dfd1fc5a1069b55d1@14.162.213.215:20156,1da145d81ca9d5d9ccd55f529435056a27fcdeef@184.174.34.227:26656,96f253c371a7f7f854faf7ffc5e0ee9fc4f8dd7f@165.227.32.93:26656,cb3335161e08c33f5cddd6e15dd441b3472e74ed@38.242.144.3:26656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656,f4fa2e13e64628d96f9158a6a2afbb19ebac574e@85.190.246.120:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,359ab5a45015c75b0ca847519254cb8d0aa3aa6c@65.108.206.74:26656,90d2b3055fc4a27fcdb4dd472c087830ecf8e42c@84.46.248.35:26656,0e90ac8e15b040c2a158b68f25299fc32a9d5940@89.117.57.25:26656,391ce347a9f0745a1f50126fcc1f9a878bacd8fe@184.174.32.55:26656,4ab5ffe672ac83bd43fcb406ae84d5f40eb73542@194.163.147.89:26656,639bf251f6fe8b1d11c322c40a44e1c0f6ebf3e7@82.208.23.171:26656,5c052c78ab48d0b26098574ba8b04e039209769a@95.217.1.96:26656,7b69fec8f71ccb56b0a2d7ddc07a92c2982a77d1@34.125.91.236:26656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,3e7ff1b1fa8626812b1ab8acf84a8b60518a8c10@65.109.88.254:34656,ba6a46ae8fe4e1e95c0debfa1d4f3012fa6b33af@66.94.123.46:26656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,9dde137d2a59bf24dd25fc2be78a56183ac56bbb@109.123.246.117:26656,668f3f60a0ff3f9fcbaf8551782f71de1cc767a9@89.116.24.215:26656,39ce82b6613c327f2bbc4cedc3a25dbf0bf8094e@38.242.252.137:26656,f4a8fb180fbbb4c44e7721368cbc6ce3f9fc47e1@5.189.140.55:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
