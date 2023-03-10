# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-4 | **Latest Version Tag**: v0.2.5 | **Wasm**: ON

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)




## Chain explorer
[https://explorer.kjnodes.com/defund-testnet](https://explorer.kjnodes.com/defund-testnet)

## Public endpoints

* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)
* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* grpc: [https://defund-testnet.grpc.kjnodes.com](https://defund-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (42)
```bash
peers="78c53aca778b1239158cf4bf6a3aeeb2239501bb@38.242.216.35:40656,3a8911a5dc4d53f2eb4174b60f2d6403529cd467@162.55.46.131:36656,1684f8e7312d55c6bb814b0966dbb0d70f53586d@148.251.91.77:21656,8675cc6e69c2043a8dc0a854e769c1f135b5f272@23.88.73.158:26656,d941341fa0f985d853f0e044d075234776cf1df6@77.232.37.54:26656,bfef03639bddf4fa503bb75c83af2b5f12c8276c@161.97.155.154:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,2b8a63defdcde856b7c4febac9658ad2ef26befb@65.108.9.230:18656,499e73f86398d0b4483e0da2b68ffbbc81d28625@38.242.131.5:26656,22e097c86358cb731fad2880291ed8e1f03b2012@65.108.78.101:26656,d1b61b43b9475e9d509f720415b75c30cb92bfb3@89.117.58.38:26656,6b94a3f12d8e694c3a735078e0cfa2b27940012a@95.214.55.62:26656,78f6683344058d2ee9fe0984b754f76bbed75621@65.109.116.110:26656,2687b608599ef656f343a790f21fb3fb9292668e@194.146.13.187:26656,6d17e0f49bc1856c732f1d439647720ba127aab8@84.46.247.5:26656,020abb71537ac87559814e1cb85cbd837046e836@23.88.5.169:23656,c9407d06e8645e860eba3ab2d2340e0d9a74c294@62.171.138.196:30656,e26206d0e39515fb07915b28e468729340eb112e@38.242.244.163:26656,38c2e79f4d9043aac5fd699d3bd5b8c3bdab0ab2@154.12.241.185:26656,2fb53d2509f3bd47fa26f39d2a2c81347c9046ef@65.108.214.39:40656,6bb4f833ad40aeddc065b6778014545c2c95b60e@173.249.47.231:27656,dca0e42d5d6838954ae08b5526c42a80c01d5538@159.69.74.237:26756,807a0dc497bec0ab730310738ef7d27fd3df7671@155.133.27.248:27656,48fe32b3f93472a26854ee6fef69447f62a265ed@199.175.98.109:26656,aa5597ed868112e494c058fd7ca4b05932074559@164.68.103.176:26656,1c4d96b6529211d2efcf4ea2e274eaff48da4ed0@65.109.70.4:40656,a39021f73cb2e6bded76c836d7ec30de6b29e618@65.21.134.250:13656,0108df8793ec07fa82ea202d54b70c603b827ea4@5.9.81.251:656,9d48e3e5307c3482ad9b0a6a8f1bee2d990facd8@78.47.100.187:40656,52a6de973b9ad92caada32c2e65655b4d92578de@65.109.2.29:26656,2726912c8b24540d1861c675d9d4bb1ae4b9dac4@154.12.238.226:40656,4df8eb475acb402f6c86b710bf1b7ac4fa7a87e9@194.146.13.254:26656,bf706069f24661022c50669b1b4a1aa95cd7766b@188.233.19.197:18656,cf61d5575997b6a67ecc71738a8c3516ce2576c4@144.91.93.32:30656,ee8b7d90655b89e1c5b76e3471fd22846e613bca@95.216.14.72:26656,278602404e78c23f5aff7a04802179ad7ffaa676@18.234.102.132:26656,051fbbbd55a1711ddbd7728eac8b4ccffa5cf9b6@65.109.5.235:26656,93153d3b1e9178f44bbbddf809a8cf7177715c03@37.221.71.67:45656,bf05df3550272f56495e9d4cf2637dd6554e36a6@38.242.139.242:26656,9d98188f51c4efd4bc04c09d985a4c490d12ebde@65.109.117.165:40656,585414640d75dd8617250c13d62c96ade9a0a1c4@65.21.147.189:26656,19f94079cc061be5c2f84539c8431d6075229669@194.4.48.96:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
