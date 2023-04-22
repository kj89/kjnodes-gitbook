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
peers="1a8e8d6667615f4836c1c1403563a26a1044fd00@116.203.158.189:26656,6b94a3f12d8e694c3a735078e0cfa2b27940012a@95.214.55.62:26656,875c807628a014aff8b4cdcbd812f183a0338d42@91.107.204.206:26656,a76e3132c3d0794302e909ff77254c012712d14b@95.217.89.106:13656,cf94df3ec5c7eca271a1d59b335ae743b2e0307d@185.215.167.45:26656,1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,9f8028ece9c514cf8f2646f8d968480b3341149f@157.90.25.62:26656,9c586a1ac70f2c921897f83cecfdfd69b0d55d8a@46.56.82.117:26656,857125a6b66826c6033a0ed7fae398d490b56261@159.69.36.152:26656,ddf6d9201f33d5d40245254bdf58ae1486b16cde@194.56.80.22:30756,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,fe3ec57e7cccb7222695c6673943b670c5a0b7f4@135.181.163.183:13656,fb124c136c3aa20a71c68d9cb0a2833293c8dc58@23.88.73.158:26656,012c382042a17adb367a092e854653475e9ba527@155.133.22.126:26656,9afc6f16f21823d3850f5d18f66de786ea9ecea5@94.130.218.86:13656,854cfaf6fd4de846fd020fbd7d0b5364c6fb9c58@65.21.95.46:27656,e0ab16d47276dee411fc01abc86c787d95ef6aba@65.109.111.204:29656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,acdac8b95e2fbe003101bda9e123d3a52951696c@62.171.143.40:26656,86caf6297ae00fb58b58a272984275c592b2fdf7@65.109.84.216:56656,e0f6aea18a4b888e00ce66f7275985b289db726e@89.163.157.64:36666,b654f4b9394fcb6a98ca5845c70bb4026aa34fda@209.145.62.91:30656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,e17ee227104d91e18c29ae1b54d60d266941b94f@135.181.200.68:27656,ba0abf77c2dec230a7ae06b32d1abf63dbd48642@5.9.82.120:60656,cdcd6ba08042b31391492666da593cc80d198cab@84.54.23.85:26656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,22fa766ffe457fd1236ea88bce1f40bf4bbaf328@77.91.100.131:26656,73657fd476a5a21f74e2f9d61ddc24709035b9c2@65.108.209.237:40656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
