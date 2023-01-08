# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.2.1 | **Wasm**: OFF

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)


## Public endpoints

* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)

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

**live-peers** (33)
```bash
peers="58d46050cf77065d27e9526a7e93c8f814cc036a@194.146.13.185:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,d8436ce4d85fac4fd245d782966bfcda312b1d54@162.55.1.2:33656,c34b4bc09946950d3fb8059d4954f45ed24e25bc@89.163.255.100:26656,d1d19e569b5dce459279e12d332bcd928abdf48b@65.109.37.58:14656,f5c51a2c40257da4524776717f91590ccad593ec@176.124.221.134:26656,34caa18dc803a7c1c5da380f85f18bbf6e2e6126@162.55.33.123:26656,4c291b33574d679e43f7cec340ba4befecec0724@161.97.152.115:26656,4eb0bef7997b87086c40766193d812479238187c@217.76.55.66:26656,58437bc62307a512f391db5c1e24e3cff8b9f8d3@136.243.88.91:2070,72ab81b6ba22876fc7f868b58efecb05ffac9753@65.109.86.236:28656,9dd945f369a7aa1946e007d9547b364e69da7db8@185.192.96.140:26656,00ddc480c7373130e1086c54173ce2bc5e0e2d45@185.190.140.81:40656,ad35b87df11c37b5f66931cd86c5dc2853aabae2@95.216.69.88:36656,d1976601f04df2a2c7e35c0e8212464acfb7512e@75.119.147.235:26656,f4869f02f970f222d81718a7a2fcf9b3c7b1b10c@109.123.249.189:26656,a28ed6c0af36097350181d5fa2d116f6e93585fe@38.242.139.91:26656,f6a16b8fd8e43442d9cbe852fa6104dc743c3383@38.242.139.242:26656,0e5c41bec481ae4da0577377bc1952eb29b1e4c1@65.21.78.86:26656,3c838e2b140d36e08c406884ab75119c016c7938@159.69.217.0:18656,a3cac2328bb41f44c17c437ff8ee29d46b91ae0c@38.242.139.95:26656,f329bee02e530e05a8937887c8ea4e75851281f1@194.180.176.126:26656,d04084623a4ec44fd91d46f07ba2e2d1d0638dd4@141.95.23.183:26656,0a1fcc2907e50b46f021389049c79f7d124f9946@77.51.200.79:36656,c734239cb2a4a59e69de4fc52a9c4aca57285391@199.175.98.107:26656,09ce2d3fc0fdc9d1e879888e7d72ae0fefef6e3d@65.108.105.48:11256,c3643415250344482ed22520e06770cdddccf5f1@185.202.223.158:26656,b5f48558fd70799ae123bd879ce12205478be379@135.125.180.36:20756,aee64a0d9b4f06f9f0949650fa22494b1cee1d58@84.46.244.228:26656,9f4ea4b9da9801ba5e97924d13c7c793d94bfec9@45.147.199.176:26656,edabbcbfb21c488be785f0925b0060c717440bad@92.119.112.229:26656,254da4ac248771ded96df539f7f70abbae5c3d93@161.97.77.186:26656,5ac71c9178d2f28b67c6c54e1b7871065aefe8da@161.97.81.155:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
