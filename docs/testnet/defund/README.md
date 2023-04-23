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

**live-peers** (29)
```bash
peers="8130e6090c692e7f43ba0b155f752251242314d2@83.167.103.215:26656,2931b7010fbbef00c06fd200e26989d903c1a249@89.163.155.252:27656,0e79b9717563b6aa14b37d04a0c128ed200765d3@188.247.44.111:26656,957b3fb47e032830e07305a3085b7c8f5fb04be4@188.247.44.126:26656,4edd4afbc38af5085172d63f5af527c48eb4f532@81.177.160.188:26656,7fe6b3e376615e9e6a0e95a6b96e8e5beebbfa3f@167.235.11.176:13656,86caf6297ae00fb58b58a272984275c592b2fdf7@65.109.84.216:56656,4d39946f5016ab24c7a62b251161dd7b1c043083@94.249.192.126:26656,2151e36f7696b39147f995c5171805c4eae0788a@194.87.113.40:26656,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,8637f94f5cc834d34244a087e370c2ec9b2590bd@75.119.132.90:26656,405c519490ef0f854b531ea99723af2aef280b2f@188.247.44.141:26656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,bc3d614b684c8e1647f4196dc8a785b1ab0381ef@65.108.13.154:33656,e3c348467a8c88c0f65e2ca8a71875d2a384b8b4@185.16.39.19:60656,0eb9422efedd714d3db57d1ddfaad75f80a60518@5.161.99.35:26656,48920dc679562d2f116f0b89ac77796377cfb130@194.146.13.254:26656,fe3ec57e7cccb7222695c6673943b670c5a0b7f4@135.181.163.183:13656,5b9504d6ba486791cee27e7d7aea247459c044ad@65.109.89.35:26656,22fa766ffe457fd1236ea88bce1f40bf4bbaf328@77.91.100.131:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,7ec94233958e634472047d9569bc59fb16379a6e@188.247.44.156:26656,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,7c459f88962a4d07d7ccd6d0c94f891bb7a7ada0@65.109.26.21:13656,dfa7af21b8c6efebe8aa6028196324f9e0540bbc@94.130.55.76:39656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,e2c541040d55eac95d9f4dca1c4e5e53d038b185@116.202.224.89:13656,79d5c2746cf510a66606ab1d9600545b311425a8@38.242.143.63:28656,773b4e59036c6934cdd3c919fc74259aba7d8ab3@185.16.39.4:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
