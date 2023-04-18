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
peers="5b9504d6ba486791cee27e7d7aea247459c044ad@65.109.89.35:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,fb124c136c3aa20a71c68d9cb0a2833293c8dc58@23.88.73.158:26656,c66d4d22039ad8afc8cc3cc873c69e2ddc37e70f@185.155.97.74:28656,82ac9dfeff1c46a985c6680022288e36aeb12ac3@65.108.40.28:61056,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,33527195a479780ce40322433f1eca5d11bc47f5@89.163.140.70:26656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,26975c5bb7dc42463cc6361ea3c75f325e801917@85.10.197.4:40656,6999cca6c55576a48d4f227b87dc904fbdb085aa@65.21.134.202:26576,5a3e8478405460c847354dc3ab84437b51b2e50b@93.185.166.71:26656,0537a8d627b65f65c810206dffef9fa820183167@65.109.160.32:40656,72e2051e1eb9163f4bd889646f775e338ae477e2@46.216.183.171:26656,bba79e883e47c07cfee15e1eae803bd063a56ea8@65.108.41.83:26656,73c4f0b46f8e6b013980ddb5196932b00b09106f@94.103.91.211:40656,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,f8036fa5e78f72606209d8022905a96364b82d19@185.209.230.110:27656,b5d6b9c758b052cd8eca8dcc4f2e0a1d5287377c@38.242.226.5:27656,93c8b8a7ca623d2a9c722b513dc57d39bf392183@46.149.76.48:26656,ef08b9e04d26c13447ef1bc965f0e1f8943d4070@95.171.21.44:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@146.59.47.207:26836,cee0d215e82cadb63f7067c8d0d7848cb24f034d@65.109.25.58:13656,11d29b833c759f5595ffdb5d0652890a8972e0bf@185.217.126.168:27656,52bbd2abd75cda2cf16238b15c103dd7ca80442f@38.242.143.147:28656,23c52b4aa95a5b269277292410f6f4c8815e616c@194.163.174.103:27656,1bffbd785051f88c84345f4114bd3092049ac1cb@144.91.106.81:26656,8639031086f7c8ce6896f924b62999812fd874f2@95.216.242.75:13656,6047d282f126e8be4b36ca28c0cc3d244577f798@159.69.185.109:26656,af9f3f65b3082007020697d035e7d5031e3be25b@212.23.222.89:26656,2788c4e5178166010baf8786ad3091a9fcc1a730@5.78.101.216:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
