# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: orbit-alpha-1 | **Latest Version Tag**: v0.2.6 | **Wasm**: ON

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/defund-testnet](https://explorer.kjnodes.com/defund-testnet)

## Public endpoints

* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)
* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* grpc: defund-testnet.grpc.kjnodes.com:40090

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

**live-peers** (26)
```bash
peers="0108df8793ec07fa82ea202d54b70c603b827ea4@5.9.81.251:60656,e73a8c70a1e55c4ee14874c659a9084773ea56ed@95.217.104.49:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,34b72721aa503574a0709b1859fb1da2aa12ce70@88.99.3.158:11256,0de10f9a019f2bfc962f51ffc706cfa40ee3fa1a@65.108.240.79:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,74e6425e7ec76e6eaef92643b6181c42d5b8a3b8@65.108.231.124:18656,e7f919a76a2462de1a1cd617f2324e24a95be3ff@164.68.113.190:26656,5d76132a47eea874b3b451182b48ae6289c2d2f3@194.146.13.253:26656,e409c0c3dc1307aebad1e112bf381c8ac8d146db@167.86.74.107:26656,6ae6e82fe96e9386e40050958f2f3722cdad9826@178.205.12.0:26656,12b1549b3d7c04d61699c2a4d6c6e5894ffd35f8@155.133.23.28:26656,0eb9422efedd714d3db57d1ddfaad75f80a60518@5.161.99.35:26656,cf28e64a237c7278223238325727cef0c2c8ca51@193.34.217.174:26656,c88bb696ecc88c3175312d04c5e3a8e2f64a3835@194.163.168.94:26656,cf94df3ec5c7eca271a1d59b335ae743b2e0307d@185.215.167.45:26656,b4df9b2eb404ec7fb12520465a2d6abfe5a8333c@147.182.150.109:26456,354485ffcd96d2c292969fae86624f754924bb8c@91.77.165.172:28656,526873de604fd6bdf1e2eec9c318adf353275fb2@31.187.74.29:26656,6e3917b457dcc1f7ac08e425125f7967d2a69c7f@194.146.13.188:26656,115c9212457522139817a7703cb5ca97d1a48c4f@81.0.247.136:26656,8230c371177d85162b32a3807428e3a34516181b@74.50.89.26:26656,b5ffc7d2fdae76bb4b2d12e370190c6ee988b172@154.53.55.153:30656,b2dab4e2f5e9ebf9901e9e8bf817af36c705b458@65.109.131.246:26456,15b81bc8c129b704bf690b482aa5d7963f3f44c0@62.171.170.79:30656,a6a8aeea2cb22e2aa18698bfd676047d2a8275a6@173.212.251.224:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
