# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: orbit-alpha-1 | **Latest Version Tag**: v0.2.6 | **Wasm**: ON

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/defund-testnet](https://explorer.kjnodes.com/defund-testnet)

## Public endpoints

* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)
* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* grpc: defund-testnet.grpc.kjnodes.com:140090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:140656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:140659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (29)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,48920dc679562d2f116f0b89ac77796377cfb130@194.146.13.254:26656,578a034282182f8ce129eedd4ef1b074ca4d3032@16.163.74.176:26616,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,beb10b655c17c4dd306c5afe51b5bcb81ff46e9c@195.128.158.119:26656,f58bf4363938c303a7ac73566a126bc2c528bd57@167.235.236.37:26456,2151e36f7696b39147f995c5171805c4eae0788a@194.87.113.40:26656,26bdbcbfa286f443c842ed241d35fa09065d586b@161.97.128.243:34656,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,0f2506a8c83b9cbeb08685829db26a4f7a0db6b0@65.21.5.11:26656,4fcbe2d0d5460ba57f48af3e0970d68715db2752@65.21.225.208:13656,fb124c136c3aa20a71c68d9cb0a2833293c8dc58@23.88.73.158:26656,a24afe4447f0712e29748742ebe3973344cdac51@78.25.145.168:40656,9bc0abcf9b7465b5026576b240655360ae8bae22@95.217.56.91:13656,41c877b907d5eae79b907ed7205b5cd363674133@65.108.78.101:26656,14cb9b8c1cfa19ba1588828996aa143a35fa88a6@185.192.96.246:26656,bccbcb85d8cecec7f6de7c1c14e1f217d85f300d@149.102.141.55:26656,773b4e59036c6934cdd3c919fc74259aba7d8ab3@185.16.39.4:26656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,4515f69283a8f3db159d35e72edce0ea0ddb6f1b@38.242.142.134:28656,354485ffcd96d2c292969fae86624f754924bb8c@91.77.165.172:28656,854cfaf6fd4de846fd020fbd7d0b5364c6fb9c58@65.21.95.46:27656,a461ba3b41468076d1a45a547dd5d9f74b017527@3.142.147.138:26656,0daf3cd2f866593b2b9f9450b3e3cfad5acc0092@45.67.231.33:26656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,424b76ff5aadcc5a58debf8e02ca251c2e521050@168.119.165.240:26456,c9ac9a9899683c6691b9bcfd7afebbb8934184a6@95.217.37.54:13656,8637f94f5cc834d34244a087e370c2ec9b2590bd@75.119.132.90:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
