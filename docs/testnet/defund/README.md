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
peers="ffb2898494cdbd6625d962ea4511c29507177c62@164.68.103.176:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,5a3e8478405460c847354dc3ab84437b51b2e50b@93.185.166.71:26656,b06b10a3e409fa503a001cec2f952f03bfd7c7d2@185.209.223.44:26656,9f8028ece9c514cf8f2646f8d968480b3341149f@157.90.25.62:26656,020abb71537ac87559814e1cb85cbd837046e836@23.88.5.169:23656,bccd2003a7eb23008479c76427ac2c276160e09a@75.119.154.72:26656,22fa766ffe457fd1236ea88bce1f40bf4bbaf328@77.91.100.131:26656,33527195a479780ce40322433f1eca5d11bc47f5@89.163.140.70:26656,274aa6457948bb8355dc8e5d3c2f7074fa699e39@37.27.7.187:26656,ee5ad3b44e90903d0bcecdbc0b4f16c4a3fa73d3@83.167.103.215:26656,fb124c136c3aa20a71c68d9cb0a2833293c8dc58@23.88.73.158:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,0e191c0d1fed5e6745bee750309a9730beacd667@178.239.197.171:26656,82ac9dfeff1c46a985c6680022288e36aeb12ac3@65.108.40.28:61056,93153d3b1e9178f44bbbddf809a8cf7177715c03@37.221.71.67:45656,c66d4d22039ad8afc8cc3cc873c69e2ddc37e70f@185.155.97.74:28656,8fdba2d059cdae2e9560ce817c1cd024b2747205@65.108.133.103:26656,5b9504d6ba486791cee27e7d7aea247459c044ad@65.109.89.35:26656,14393b49195fc9496191d5091e53c9c2f55da648@62.183.54.219:40656,11c0952beaf78a6452d270c7bd344c25406e1b16@95.217.212.66:26656,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,86caf6297ae00fb58b58a272984275c592b2fdf7@65.109.84.216:56656,93c8b8a7ca623d2a9c722b513dc57d39bf392183@46.149.76.48:26656,ed9d651a48968b4c3c8e8f01e15dbb451eed195a@5.75.138.108:26656,73a560b069d3ab8991ff83a8d2f3453d891e05c6@92.55.63.130:32656,bda598af0c96d72a85c3b6840138d929b8c4e762@84.46.248.207:26656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,0108df8793ec07fa82ea202d54b70c603b827ea4@5.9.81.251:60656,a2ece73a10efc3479af801647e9a98b39325b6db@65.21.141.104:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
