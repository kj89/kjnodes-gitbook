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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,8637f94f5cc834d34244a087e370c2ec9b2590bd@75.119.132.90:26656,beb10b655c17c4dd306c5afe51b5bcb81ff46e9c@195.128.158.119:26656,8274cf9149b23c23694cdce7045a607879fc51b2@95.217.182.26:26456,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,2425a645f1b375c4d61857a7010841d4baf74a1b@109.195.131.79:36656,afdbe2fb845ff591d32f83e4a28b49c59cd9111c@65.109.117.121:13656,fb95f32da1b85cb4c1fa04c2e75b045352a5507f@5.104.108.71:26656,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,2151e36f7696b39147f995c5171805c4eae0788a@194.87.113.40:26656,b44266dc79cf178ca2bc690bcae949efffe77ae7@51.15.0.91:26656,c2974fd847a286f1b960f5a7a63b96f582c88f48@207.244.227.247:26656,424b76ff5aadcc5a58debf8e02ca251c2e521050@168.119.165.240:26456,0f2506a8c83b9cbeb08685829db26a4f7a0db6b0@65.21.5.11:26656,4d39946f5016ab24c7a62b251161dd7b1c043083@94.249.192.126:26656,01eb6fc83d3ef9757696c2f72ab7cc3c2cd393e7@193.34.217.183:26656,f114c02efc5aa7ee3ee6733d806a1fae2fbfb66b@5.9.147.22:25656,7c459f88962a4d07d7ccd6d0c94f891bb7a7ada0@65.109.26.21:13656,d7b1896a0dad8f7c5d77cb8656271c972120ce55@154.53.54.154:30656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,e65e04d46c74e9f180befc01d5772178e2180897@65.109.154.182:33656,bccd2003a7eb23008479c76427ac2c276160e09a@75.119.154.72:26656,8a650a9761db8abc1096abc3d4a68431600ae835@62.171.149.101:46656,773b4e59036c6934cdd3c919fc74259aba7d8ab3@185.16.39.4:26656,b49d37bcff2dfa85108dfb51c6b5e45444b6a57f@65.109.30.12:26656,206310423b4a8e09115d824bee3a6595d93d86c8@89.163.151.193:26656,0108df8793ec07fa82ea202d54b70c603b827ea4@5.9.81.251:60656,d0c6f2febf03bbf69a3cd1c5fb489d7febfc34b9@65.109.116.119:40656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
