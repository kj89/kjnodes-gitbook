# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.1.0 | **Wasm**: OFF

Website: [https://www.defund.app](https://www.defund.app)


## Public endpoints

* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (31)
```
peers="507e7ea5c2c97d411f66238b97d7e7d931800977@116.202.161.165:29656,01a4dbeb9cdb8fc7086199a7111381735f4c5f41@176.9.106.43:26656,db1b1a1350e3bf1815603024dc7dcc4ef76053b6@65.109.82.106:40656,997da62262006ce89d5019b7820b5552118e0df2@138.201.17.11:28656,f9fcb1705d112b357fa498bb0711e2f4953d3f88@195.201.237.188:18656,0e5c41bec481ae4da0577377bc1952eb29b1e4c1@65.21.78.86:26656,9dd904e70deef1042fc8a0802381fb083f83dc39@5.199.143.159:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,13e13cc3b1cee183592bffc1aaae6a9b3b7a7e20@38.242.206.62:40656,760bc7fc66c15c9f2b9d722b9ee673cbdd265614@144.76.97.251:31256,667f6c6d694bcd6743e6f42bb6e5996c4c9f16dd@84.244.31.1:26656,c0b96875a8d2b8ff587c618e388ab3268bb586bf@154.12.246.0:26656,20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,00ddc480c7373130e1086c54173ce2bc5e0e2d45@185.190.140.81:40656,75e38d35a430a9c1ac65249db3d4cab245159a8b@144.91.97.124:26656,5f27d363c126cf7f7e1e9cab2dadd62862109e3d@65.21.227.112:26656,fe32ed5f0a7f8928f8299d8dd78fc5b650472ac4@65.108.46.123:56656,3441bf28387afc7d9b6e7a754c3ed37f21006859@5.161.134.231:26656,67742399a48abc97c7eef61b1a60b96c720122c2@45.147.199.180:26656,2218acbe81b1f57da84cf0db5ebb6fe65e5e3362@188.34.178.188:18656,cdd1107a3f013e4bfdd8e549e94b7e54ec18bd09@142.132.199.236:23656,b5252eac7b8bc4d5d2cc211bc794f8b4e62d2cc4@188.34.154.116:26656,0f8c0605d9b8004332fbcaeaaababbbf9002e4df@135.181.253.11:18656,b50363075f36fa3382f78bdbe0c297dd27465eeb@154.38.161.212:26656,c34b4bc09946950d3fb8059d4954f45ed24e25bc@89.163.255.100:26656,9ae365f1c4a2b95c95fdcaa92db4a4f5a655ef1f@5.161.108.72:26656,7831e762e13c2cb99236b59f5513bf1f8d16d036@88.99.3.158:10356,409d5422d6934b0dedfd3347e078b67aac691120@45.147.199.185:26656,89944fe8fc90920cdd95ac8b752b81524c357961@38.242.234.75:26656,04bdf241c94c3d59c34b5496b012279f099a6cca@168.119.89.31:33656,9f4ea4b9da9801ba5e97924d13c7c793d94bfec9@45.147.199.176:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
