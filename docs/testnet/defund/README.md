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

**live-peers** (30)
```bash
peers="6ebe0fd3fd0990feec2dd1e09fe06b766b6b67d0@65.109.92.79:18656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,fb124c136c3aa20a71c68d9cb0a2833293c8dc58@23.88.73.158:26656,7cf71585a37706c20a0a72bbe283439af30873ab@173.249.47.194:26656,33527195a479780ce40322433f1eca5d11bc47f5@89.163.140.70:26656,37fcbac03dec1b0b717faf074e76d12865884293@194.163.191.213:27656,7b1f3e49e2a21e59e11e434e3bb8907d4d3705d1@65.21.202.160:13656,185401b61cbe26895b5a7c025e8666349c3129ff@213.133.97.154:13656,ed9d651a48968b4c3c8e8f01e15dbb451eed195a@5.75.138.108:26656,34b72721aa503574a0709b1859fb1da2aa12ce70@88.99.3.158:11256,7c459f88962a4d07d7ccd6d0c94f891bb7a7ada0@65.109.26.21:13656,bda598af0c96d72a85c3b6840138d929b8c4e762@84.46.248.207:26656,82ac9dfeff1c46a985c6680022288e36aeb12ac3@65.108.40.28:61056,5a3e8478405460c847354dc3ab84437b51b2e50b@93.185.166.71:26656,0e191c0d1fed5e6745bee750309a9730beacd667@178.239.197.171:26656,773b4e59036c6934cdd3c919fc74259aba7d8ab3@185.16.39.4:26656,a2ece73a10efc3479af801647e9a98b39325b6db@65.21.141.104:13656,9d62097edd303eefe1ea7b4a51a76e50d09cdada@185.16.39.13:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@146.59.47.207:26836,73a560b069d3ab8991ff83a8d2f3453d891e05c6@92.55.63.130:32656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,7cf6dc70e9dfa82db373120de0d79dddc71bd74e@194.34.232.99:26656,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,8c4bb6fac15cf74f5475cbc2fcb5ad5902ffa164@149.102.136.173:27656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,23c52b4aa95a5b269277292410f6f4c8815e616c@194.163.174.103:27656,fa3970a28ad03db88f316ae0a56908432cee5f5d@65.21.141.248:13656,9446504166663fc0090b81abdf86fafe93e72a40@185.209.30.95:40656,969592457e566730a8894c04ab16e2018735d7ab@95.216.2.219:26656,11c0952beaf78a6452d270c7bd344c25406e1b16@95.217.212.66:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
