# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-4 | **Latest Version Tag**: v0.2.2 | **Wasm**: OFF

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)


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

**live-peers** (17)
```bash
peers="16af5142a97d6bd22f941c15ad8faf2150d48e59@157.90.157.18:26656,8675cc6e69c2043a8dc0a854e769c1f135b5f272@23.88.73.158:26656,75cccc67bc20e7e5429b80c4255ffe44ef24bc26@65.109.85.170:33656,acad4439671fef4e64e904587a81ee9c34e9505d@95.216.214.103:40656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,d9f1a0f399c8db62206edb2be29a313829fc8521@135.181.128.19:26656,01b73409f0a44e9998af038259ce079af906c405@65.109.167.54:26656,9f4ea4b9da9801ba5e97924d13c7c793d94bfec9@45.147.199.176:26656,0ab2ceb8999da66cd9eeaa6d7f0e3144c1f7a31e@89.108.109.116:26656,e104f008f6d1227170d3b4ce1d73f0ea2068094f@84.201.162.168:26656,219c417bd9de04c60f730abd4769e981f10c083b@109.123.249.191:26656,0176c2127c25f0ecd8383577cd373e0928d20884@86.48.3.14:26656,4eb0bef7997b87086c40766193d812479238187c@217.76.55.66:26656,b32e6619a1c7998519d2d38828e34ace7b773852@65.109.84.250:26656,4d3b782ab389525370f53d40e970b1362bc92106@185.182.186.202:26656,c675bd639c81562cb52e2b14bae0cbaaf78150bf@84.46.249.51:26656,fb73921dc5bf1e939308eaa37053c12bd647852b@45.147.199.210:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
