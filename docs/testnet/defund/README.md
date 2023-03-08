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

**live-peers** (30)
```bash
peers="ba0abf77c2dec230a7ae06b32d1abf63dbd48642@5.9.82.120:61656,6854d36513081c77a24987ab66a436e29e3e5cfa@65.21.131.215:26576,1684f8e7312d55c6bb814b0966dbb0d70f53586d@148.251.91.77:21656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,8675cc6e69c2043a8dc0a854e769c1f135b5f272@23.88.73.158:26656,dca0e42d5d6838954ae08b5526c42a80c01d5538@159.69.74.237:26756,41da85e7d2508400bc5a6d3843a1b0e258243985@155.133.22.128:26656,bf6472ff84ececf1108538b994931f23cb198892@65.109.3.8:26656,2b8a63defdcde856b7c4febac9658ad2ef26befb@65.108.9.230:18656,e21aa9dfe1a522453bb89a290cf49a476cf38bea@65.21.58.9:40656,d1b61b43b9475e9d509f720415b75c30cb92bfb3@89.117.58.38:26656,a240dbc941bdf485d46191a4db4ce2d0fe69cc1f@164.68.127.182:26656,da7e109ceb4376c812267062fddf98f01ec834df@40.83.10.226:26656,78f6683344058d2ee9fe0984b754f76bbed75621@65.109.116.110:26656,a82e76d4c9e2f3caf5c9b28a7ce48be7374f122d@161.35.90.88:26656,6d17e0f49bc1856c732f1d439647720ba127aab8@84.46.247.5:26656,2687b608599ef656f343a790f21fb3fb9292668e@194.146.13.187:26656,c2977e5d8d822e75c8916867b5c713e6b3841705@65.109.225.137:40656,8929e0ccc72aea2de41bd97aa636d25c01832ac2@62.141.45.243:26656,22e097c86358cb731fad2880291ed8e1f03b2012@65.108.78.101:26656,e26206d0e39515fb07915b28e468729340eb112e@38.242.244.163:26656,38c2e79f4d9043aac5fd699d3bd5b8c3bdab0ab2@154.12.241.185:26656,d089beab9fcccd6b95217f0972831d6d861a9009@164.68.109.229:26656,f393c1e540566d94ee840ef64431136b1d35d3a6@5.189.159.198:28656,bfef03639bddf4fa503bb75c83af2b5f12c8276c@161.97.155.154:26656,6bb4f833ad40aeddc065b6778014545c2c95b60e@173.249.47.231:27656,48fe32b3f93472a26854ee6fef69447f62a265ed@199.175.98.109:26656,1c4d96b6529211d2efcf4ea2e274eaff48da4ed0@65.109.70.4:40656,2b76e96658f5e5a5130bc96d63f016073579b72d@51.91.215.40:45656,8e5a383750402ff60c803a7554e470c4041340a1@46.4.101.82:40656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
